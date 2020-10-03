from enum import IntEnum, unique
from typing import Union

from . import zint


@unique
class Barcode(IntEnum):
    # Tbarcode 7 codes
    CODE11 = zint.BARCODE_CODE11
    C25MATRIX = zint.BARCODE_C25MATRIX
    C25INTER = zint.BARCODE_C25INTER
    C25IATA = zint.BARCODE_C25IATA
    C25LOGIC = zint.BARCODE_C25LOGIC
    C25IND = zint.BARCODE_C25IND
    CODE39 = zint.BARCODE_CODE39
    EXCODE39 = zint.BARCODE_EXCODE39
    EANX = zint.BARCODE_EANX
    EANX_CHK = zint.BARCODE_EANX_CHK
    EAN128 = zint.BARCODE_EAN128
    CODABAR = zint.BARCODE_CODABAR
    CODE128 = zint.BARCODE_CODE128
    DPLEIT = zint.BARCODE_DPLEIT
    DPIDENT = zint.BARCODE_DPIDENT
    CODE16K = zint.BARCODE_CODE16K
    CODE49 = zint.BARCODE_CODE49
    CODE93 = zint.BARCODE_CODE93
    FLAT = zint.BARCODE_FLAT
    RSS14 = zint.BARCODE_RSS14
    RSS_LTD = zint.BARCODE_RSS_LTD
    RSS_EXP = zint.BARCODE_RSS_EXP
    TELEPEN = zint.BARCODE_TELEPEN
    UPCA = zint.BARCODE_UPCA
    UPCA_CHK = zint.BARCODE_UPCA_CHK
    UPCE = zint.BARCODE_UPCE
    UPCE_CHK = zint.BARCODE_UPCE_CHK
    POSTNET = zint.BARCODE_POSTNET
    MSI_PLESSEY = zint.BARCODE_MSI_PLESSEY
    FIM = zint.BARCODE_FIM
    LOGMARS = zint.BARCODE_LOGMARS
    PHARMA = zint.BARCODE_PHARMA
    PZN = zint.BARCODE_PZN
    PHARMA_TWO = zint.BARCODE_PHARMA_TWO
    PDF417 = zint.BARCODE_PDF417
    PDF417TRUNC = zint.BARCODE_PDF417TRUNC
    MAXICODE = zint.BARCODE_MAXICODE
    QRCODE = zint.BARCODE_QRCODE
    CODE128B = zint.BARCODE_CODE128B
    AUSPOST = zint.BARCODE_AUSPOST
    AUSREPLY = zint.BARCODE_AUSREPLY
    AUSROUTE = zint.BARCODE_AUSROUTE
    AUSREDIRECT = zint.BARCODE_AUSREDIRECT
    ISBNX = zint.BARCODE_ISBNX
    RM4SCC = zint.BARCODE_RM4SCC
    DATAMATRIX = zint.BARCODE_DATAMATRIX
    EAN14 = zint.BARCODE_EAN14
    VIN = zint.BARCODE_VIN
    CODABLOCKF = zint.BARCODE_CODABLOCKF
    NVE18 = zint.BARCODE_NVE18
    JAPANPOST = zint.BARCODE_JAPANPOST
    KOREAPOST = zint.BARCODE_KOREAPOST
    RSS14STACK = zint.BARCODE_RSS14STACK
    RSS14STACK_OMNI = zint.BARCODE_RSS14STACK_OMNI
    RSS_EXPSTACK = zint.BARCODE_RSS_EXPSTACK
    PLANET = zint.BARCODE_PLANET
    MICROPDF417 = zint.BARCODE_MICROPDF417
    ONECODE = zint.BARCODE_ONECODE
    PLESSEY = zint.BARCODE_PLESSEY

    # Tbarcode 8 codes
    TELEPEN_NUM = zint.BARCODE_TELEPEN_NUM
    ITF14 = zint.BARCODE_ITF14
    KIX = zint.BARCODE_KIX
    AZTEC = zint.BARCODE_AZTEC
    DAFT = zint.BARCODE_DAFT
    MICROQR = zint.BARCODE_MICROQR

    # Tbarcode 9 codes
    HIBC_128 = zint.BARCODE_HIBC_128
    HIBC_39 = zint.BARCODE_HIBC_39
    HIBC_DM = zint.BARCODE_HIBC_DM
    HIBC_QR = zint.BARCODE_HIBC_QR
    HIBC_PDF = zint.BARCODE_HIBC_PDF
    HIBC_MICPDF = zint.BARCODE_HIBC_MICPDF
    HIBC_BLOCKF = zint.BARCODE_HIBC_BLOCKF
    HIBC_AZTEC = zint.BARCODE_HIBC_AZTEC

    # Tbarcode 10 codes
    DOTCODE = zint.BARCODE_DOTCODE
    HANXIN = zint.BARCODE_HANXIN

    # Tbarcode 11 codes
    MAILMARK = zint.BARCODE_MAILMARK

    # Zint specific
    AZRUNE = zint.BARCODE_AZRUNE
    CODE32 = zint.BARCODE_CODE32
    EANX_CC = zint.BARCODE_EANX_CC
    EAN128_CC = zint.BARCODE_EAN128_CC
    RSS14_CC = zint.BARCODE_RSS14_CC
    RSS_LTD_CC = zint.BARCODE_RSS_LTD_CC
    RSS_EXP_CC = zint.BARCODE_RSS_EXP_CC
    UPCA_CC = zint.BARCODE_UPCA_CC
    UPCE_CC = zint.BARCODE_UPCE_CC
    RSS14STACK_CC = zint.BARCODE_RSS14STACK_CC
    RSS14_OMNI_CC = zint.BARCODE_RSS14_OMNI_CC
    RSS_EXPSTACK_CC = zint.BARCODE_RSS_EXPSTACK_CC
    CHANNEL = zint.BARCODE_CHANNEL
    CODEONE = zint.BARCODE_CODEONE
    GRIDMATRIX = zint.BARCODE_GRIDMATRIX
    UPNQR = zint.BARCODE_UPNQR
    RMQR = zint.BARCODE_RMQR

    def __call__(self, data: Union[str, bytes], *args, **kwargs) -> zint.Zint:
        return zint.Zint(data, self.value, *args, **kwargs)


__all__ = [
    Barcode,
]
