from enum import Enum


class Approval(Enum):
    AP = "Setujui"
    RJ = "Tolak"


class Fluctuate(Enum):
    TR = 'Fluktuatif'
    FL = 'Flat'


class Choice(Enum):
    YES = 'Ya'
    NO = 'Tidak'


class Sex(Enum):
    ML = "Pria"
    FM = "Wanita"


class FamilyMember(Enum):
    PR = "Orang Tua"
    BS = "Kakak Kandung"
    LS = "Adik Kandung"
    CL = "Anak berusia 18+"


class HousingType(Enum):
    HS = "Rumah"
    AP = "Apartment"
    SH = "Ruko"


class HsOwnerType(Enum):
    IN = "Angsuran"
    FH = "Milik Keluarga"
    CH = "Milik Perusahaan"
    OW = "Milik Pribadi"
    IK = "Kost"
    RT = "Sewa"


class JobsType(Enum):
    EB = "Pegawai BUMN"
    EP = "Pegawai Swasta"
    EG = "Pegawai Negeri"
    DC = "Dokter"
    LG = "Pengacara"
    BM = "Pemilik Perusahaan"
    OD = "Driver Online"
    EH = "Pekerja Paruh Waktu"
    ST = "Pelajar"
    NW = "Tidak Bekerja"


class JobsIndustry(Enum):
    AF = "Asuransi / Forex"
    HP = "Hukum dan Perpajakan"
    IP = "Industri / Pabrik"
    JL = "Jasa / Layanan"
    KK = "Kesehatan / Klinik"
    KB = "Keuangan / Bank"
    KS = "Konsultan"
    KP = "Kontraktor / Properti"
    PW = "Pariwisata"
    GP = "Pemerintahan"
    PD = "Perdagangan"
    PK = "Perkebunan"
    PT = "Pertambangan"
    RT = "Restaurant / Cafe / Bar"
    RL = "Retail"
    SP = "Spesialis"
    TK = "Telekomunikasi"
    TP = "Transportasi"


class LoanType(Enum):
    EL = "Keperluan Pribadi"
    BE = "Pengembangan Usaha"


class WebPageLoc(Enum):
    EL = "Insert"
    BE = "Create"


class TypeTrans(Enum):
    CR = "Credit"
    DB = "Debit"
    PY = "Payment"
    IS = "Investment"
    TR = "Transfer"


class Ziswaf(Enum):
    ZT = 'Zakat'
    IN = 'Infaq'
    SD = 'Shadaqah'
    WQ = 'Waqaf'
    

class Marital(Enum):
    SG = "Lanjang"
    MG = "Menikah"
    DV = "Cerai / Pisah"
    
    
class Education(Enum):
    EL = "SD"
    JH = "SMP / SLTP"
    HS = "SMK / SMA"
    S1 = "Strata 1"
    S2 = "Strata 2"
    S3 = "Strata 3"