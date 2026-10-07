#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nakłada poprawki Serie D (wersja "v14") na FM2008 fm.exe 8.0.2 (ProductVersion 8.0.2f117931, znacznik czasu PE 0x47B3C3C6).

Użycie:  python apply_serieD_v14.py fm.exe fm_serieD_v14.exe

Wejście: oryginalny fm.exe (plik 0x1537000 = 22 245 376 B, 4 sekcje) albo plik, który
już ma sekcję .mycode. Skrypt:
  1. dodaje (albo powiększa) sekcję .mycode do 0x2000 bajtów,
  2. sprawdza oczekiwane bajty w każdym miejscu poprawki i przerywa przy niezgodności,
  3. zapisuje 3 hooki, 2 sloty tablicy wirtualnej i 4 bloki kodu w .mycode.
Skrypt nie nadpisuje pliku wejściowego. Opis każdej poprawki jest w dokumentacji (sekcja 5).
"""
import struct, sys, base64

IMAGE_BASE   = 0x400000
MYCODE_VA    = 0x1C04000
MYCODE_RVA   = MYCODE_VA - IMAGE_BASE        # 0x1804000
MYCODE_FO    = 0x1537000                     # offset sekcji w pliku = rozmiar oryginału
MYCODE_SIZE  = 0x2000
PRISTINE_LEN = 0x1537000
SECTION_FLAGS = 0x60000020                   # kod | wykonywalna | do odczytu

# --- bloki kodu w .mycode (VA -> bajty) ---------------------------------------------
CAVE_A = bytes.fromhex("6a096a04686db00c008bcee800f915ff6a038bce885e11e9445c2fff")      # 0x1C04300: D63C10(0xCB06D, poziom 4, 9 grup) + oryginał
CAVE_B = bytes.fromhex("8b5500817d146db00c00750732c0e99c351bff6a018bcdff5268e990351bff")      # 0x1C04440: wąski hook relegacji (para C2-D)
CAVE_C = bytes.fromhex("8b4c242c817d146db00c0075388b854802000085c07e2e0fb754242485d274254a39c2720429c2ebf88b854402000085c074128b049085c0740b894754894f5ce96ef01aff896f54894f5ce963f01aff")      # 0x1C05200: przydział klubów z puli do grup D
SETTINGS_COPY_B64 = """
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
AgAAwggA
"""                                          # 0x1C04500: kopia ustawień C2 (3027 B), slot 88 grupy D
SETTINGS_COPY = base64.b64decode("".join(SETTINGS_COPY_B64.split()))
assert len(SETTINGS_COPY) == 3027

CODE_BLOCKS = {0x1C04300: CAVE_A, 0x1C04440: CAVE_B, 0x1C05200: CAVE_C, 0x1C04500: SETTINGS_COPY}

# --- hooki w oryginalnym kodzie: (VA, oczekiwane bajty, cel jaskini, liczba NOP-ów) ---
HOOKS = [
    (0xEF9F59, bytes.fromhex("6a038bce885e11"),          0x1C04300),   # ita_get_settings: rejestracja poziomu 4
    (0xDB79E5, bytes.fromhex("8b55006a018bcdff5268"),    0x1C04440),   # FUN_00DB74A0: wyjątek dla pary (C2, D)
    (0xDB42A9, bytes.fromhex("8b4c242c896f54894f5c"),    0x1C05200),   # FUN_00DB40A0: kluby z puli do grup
]
# --- sloty tablicy wirtualnej ITA_D_DIVISION (główna vtable 0x1657DEC) ---------------
VTABLE_SLOTS = [
    (0x1657DEC + 86 * 4, 0x5172A0, 0xEFF010),     # slot 86: stub -> forwarder C2 (dopięcie etapu)
    (0x1657DEC + 88 * 4, 0xA3ACB0, 0x1C04500),    # slot 88: NULL -> kopia ustawień C2
]
# --- stary hook, który trzeba mieć wycofany ---------------------------------------
HOOK3_VA, HOOK3_ORIG = 0xF06B48, bytes.fromhex("5e5b59c3cc")

def fo(va):
    """VA -> offset w pliku (.text, .rdata, .data oraz .mycode)."""
    if MYCODE_VA <= va < MYCODE_VA + MYCODE_SIZE:
        return MYCODE_FO + (va - MYCODE_VA)
    if 0x401000 <= va < 0x1BE0000:
        return va - IMAGE_BASE
    raise ValueError(hex(va))

def pe_offsets(d):
    pe = struct.unpack_from("<I", d, 0x3C)[0]
    assert d[pe:pe+4] == b"PE\0\0"
    nsec = struct.unpack_from("<H", d, pe + 6)[0]
    opt_size = struct.unpack_from("<H", d, pe + 0x14)[0]
    return pe, pe + 6, pe + 0x18 + 0x38, pe + 0x18 + opt_size, nsec     # pe, NumberOfSections, SizeOfImage, tablica sekcji, n

def ensure_mycode(d):
    d = bytearray(d)
    pe, off_nsec, off_soi, sec_tab, nsec = pe_offsets(d)
    found = None
    for i in range(nsec):
        o = sec_tab + 40 * i
        if d[o:o+8].rstrip(b"\0") == b".mycode":
            found = o
    if found is None:
        assert len(d) == PRISTINE_LEN, "oczekiwano oryginału o rozmiarze 0x1537000 (albo pliku z sekcja .mycode)"
        o = sec_tab + 40 * nsec
        assert d[o:o+40] == bytes(40), "brak miejsca w tablicy sekcji na nowy nagłówek"
        hdr = b".mycode\0" + struct.pack("<IIIIIIHHI", MYCODE_SIZE, MYCODE_RVA, MYCODE_SIZE, MYCODE_FO, 0, 0, 0, 0, SECTION_FLAGS)
        d[o:o+40] = hdr
        struct.pack_into("<H", d, off_nsec, nsec + 1)
        d.extend(bytes(MYCODE_SIZE))
    else:
        vsize, rva, rsize, rptr = struct.unpack_from("<IIII", d, found + 8)
        assert rptr == MYCODE_FO and rva == MYCODE_RVA, "sekcja .mycode w innym miejscu niż oczekiwano"
        if rsize < MYCODE_SIZE:
            struct.pack_into("<I", d, found + 8, MYCODE_SIZE)
            struct.pack_into("<I", d, found + 16, MYCODE_SIZE)
            d.extend(bytes(MYCODE_SIZE - rsize))
    soi = struct.unpack_from("<I", d, off_soi)[0]
    need = MYCODE_RVA + MYCODE_SIZE
    if soi < need:
        struct.pack_into("<I", d, off_soi, need)
    return d

def main(src, dst):
    if src == dst:
        sys.exit("plik wyjściowy musi się różnić od wejściowego")
    d = ensure_mycode(open(src, "rb").read())
    # 0) kontrola starego hooka 0xF06B48
    o = fo(HOOK3_VA)
    if d[o:o+5] != HOOK3_ORIG:
        if d[o] == 0xE9:
            print("UWAGA: pod 0xF06B48 jest stary hook (powodował awarie) - przywracam oryginał")
            d[o:o+5] = HOOK3_ORIG
        else:
            sys.exit("0xF06B48: nieoczekiwane bajty " + d[o:o+5].hex())
    # 1) bloki kodu: miejsce musi być puste albo już zawierać ten sam kod
    for va, code in CODE_BLOCKS.items():
        o = fo(va)
        cur = bytes(d[o:o+len(code)])
        if cur not in (bytes(len(code)), code):
            sys.exit("0x%X: miejsce w .mycode jest zajęte innym kodem" % va)
        d[o:o+len(code)] = code
    # 2) hooki
    for va, expect, cave in HOOKS:
        o = fo(va)
        cur = bytes(d[o:o+len(expect)])
        hook = b"\xe9" + struct.pack("<i", cave - (va + 5)) + b"\x90" * (len(expect) - 5)
        if cur == hook:
            continue
        if cur != expect:
            sys.exit("0x%X: oczekiwano %s, jest %s" % (va, expect.hex(), cur.hex()))
        d[o:o+len(expect)] = hook
    # 3) sloty vtable
    for va, old, new in VTABLE_SLOTS:
        o = fo(va)
        cur = struct.unpack_from("<I", d, o)[0]
        if cur not in (old, new):
            sys.exit("slot 0x%X: oczekiwano 0x%X, jest 0x%X" % (va, old, cur))
        struct.pack_into("<I", d, o, new)
    open(dst, "wb").write(d)
    print("OK: zapisano", dst, "(%d B)" % len(d))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
