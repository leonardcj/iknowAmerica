# -*- coding: utf-8 -*-

from gettext import gettext as _

NAME = _('Peru')

STATES = [
    (_('Tumbes'), 254, 138, 204, 0),
    (_('Loreto'), 253, 413, 216, 0),
    (_('Piura'), 252, 150, 267, 0),
    (_('Amazonas'), 251, 253, 261, 90),
    (_('Cajamarca'), 250, 217, 320, 90),
    (_('Lambayeque'), 249, 135, 326, 0),
    (_('San Martín'), 248, 320, 370, -45),
    (_('La Libertad'), 247, 234, 414, 30),
    (_('Ancash'), 246, 277, 468, -60),
    (_('Huanuco'), 245, 361, 476, 0),
    (_('Lima'), 244, 329, 575, -60),
    (_('Cerro de Pasco'), 243, 386, 511, 20),
    (_('Junín'), 242, 404, 566, 0),
    (_('Ucayali'), 241, 515, 517, 0),
    (_('Madre de Dios'), 240, 605, 587, 0),
    (_('Cuzco'), 239, 529, 634, -30),
    (_('Ica'), 238, 380, 697, -45),
    (_('Huancavelica'), 237, 400, 634, 45),
    (_('Ayacucho'), 236, 441, 689, 90),
    (_('Arequipa'), 235, 523, 765, 0),
    (_('Apurimac'), 234, 507, 679, 0),
    (_('Puno'), 233, 632, 698, 45),
    (_('Moquegua'), 232, 591, 812, 45),
    (_('Tacna'), 231, 616, 845, 45),
    (_('Brazil'), 230, 646, 363, 0),
    (_('Ecuador'), 229, 228, 91, 0),
    (_('Colombia'), 228, 536, 56, 0),
    (_('Bolivia'), 227, 734, 710, 90)
]

CAPITALS = [
    (_('Lima'), 316, 590, 0, 0, 14),
    (_('Abancay'), 501, 657, 1, 0, 14),
    (_('Arequipa'), 560, 786, 1, 0, -14),
    (_('Ayacucho'), 438, 636, 1, 0, 14),
    (_('Cajamarca'), 239, 358, 1, 20, 14),
    (_('Callao'), 309, 579, 1, 0, -14),
    (_('Cerro de Pasco'), 346, 522, 1, 30, 14),
    (_('Chachapoyas'), 268, 314, 1, -10, 14),
    (_('Chiclayo'), 178, 341, 1, -25, -14),
    (_('Cusco'), 542, 653, 1, 0, -14),
    (_('Huánuco'), 349, 485, 1, 15, 14),
    (_('Huancavelica'), 402, 616, 1, 65, 0),
    (_('Huancayo'), 394, 586, 1, 50, 0),
    (_('Huaraz'), 287, 469, 1, 10, 14),
    (_('Ica'), 367, 676, 1, 20, 0),
    (_('Iquitos'), 487, 204, 1, 0, -14),
    (_('Moquegua'), 588, 819, 1, 15, 14),
    (_('Moyobamba'), 314, 307, 1, 20, -14),
    (_('Piura'), 140, 271, 1, 0, 14),
    (_('Pucallpa'), 424, 413, 1, 20, 14),
    (_('Puerto Maldonado'), 669, 612, 1, 10, 14),
    (_('Puno'), 627, 763, 1, 0, 14),
    (_('Tacna'), 617, 860, 1, 0, 14),
    (_('Trujillo'), 217, 402, 1, 0, 14),
    (_('Tumbes'), 147, 195, 1, 0, -14)
]

CITIES = [
    (_('Azángaro'), 618, 716, 2, 0, -14),
    (_('Bagua'), 235, 286, 2, 0, -14),
    (_('Barranca'), 276, 520, 2, -50, 0),
    (_('Caballococha'), 616, 211, 2, 0, 14),
    (_('Camana'), 517, 796, 2, -45, 0),
    (_('Caraveli'), 476, 762, 2, -10, 14),
    (_('Casma'), 251, 467, 2, -40, 0),
    (_('Chimbote'), 240, 446, 2, -50, 0),
    (_('Chincha Alta'), 353, 647, 2, -60, 0),
    (_('Contamana'), 402, 363, 2, 0, 14),
    (_('Coracora'), 460, 723, 2, 10, -14),
    (_('Cotahuasi'), 496, 729, 2, 15, 14),
    (_('Flor de Agosto'), 492, 140, 2, 0, 14),
    (_('Huacho'), 288, 542, 2, -45, 0),
    (_('Huarmey'), 259, 492, 2, -45, 0),
    (_('Iñapari'), 650, 540, 2, 0, 14),
    (_('Juliaca'), 623, 744, 2, 10, -14),
    (_('La Oroya'), 361, 563, 2, 40, 0),
    (_('Macusani'), 613, 679, 2, 0, -14),
    (_('Manú'), 593, 593, 2, 0, -14),
    (_('Mollendo'), 540, 812, 2, -45, 0),
    (_('Nauta'), 468, 232, 2, 0, 14),
    (_('Nazca'), 407, 715, 2, 0, 14),
    (_('Palpa'), 396, 701, 2, -35, 0),
    (_('Pisco'), 355, 667, 2, -35, 0),
    (_('Puerto Inca'), 408, 460, 2, 25, 14),
    (_('Requena'), 459, 262, 2, 0, 14),
    (_('San Pedro de Lloc'), 193, 371, 2, -80, 0),
    (_('San Vicente de Cañete'), 342, 631, 2, -100, 0),
    (_('Sullana'), 139, 255, 2, 20, -14),
    (_('Talara'), 110, 243, 2, -20, -14),
    (_('Tarapoto'), 339, 328, 2, 20, 14),
    (_('Tingo Maria'), 361, 449, 2, -10, -14)
]

RIVERS = [
    (_('Napo River'), 254, 386, 61, -30),
    (_('Curaray River'), 253, 377, 92, -30),
    (_('Tigre River'), 252, 390, 159, -45),
    (_('Corrientes River'), 251, 362, 178, -45),
    (_('Pastaza River'), 250, 285, 135, -40),
    (_('Amazonas River'), 249, 601, 195, 0),
    (_('Javari River'), 248, 523, 275, 45),
    (_('Juruá River'), 247, 495, 440, 90),
    (_('Acre River'), 246, 717, 508, 45),
    (_('Iaco River'), 245, 642, 505, 30),
    (_('Alto Purús River'), 244, 600, 458, 45),
    (_('Madre de Dios River'), 243, 716, 576, 45),
    (_('Piedras River'), 242, 610, 575, -45),
    (_('Inambari River'), 241, 627, 679, -50),
    (_('Putumayo River'), 240, 573, 121, 0),
    (_('Marañón River'), 239, 265, 389, -65),
    (_('Santiago River'), 238, 228, 180, 60),
    (_('Huallaga River'), 237, 336, 326, 60),
    (_('Ucayali River'), 236, 413, 422, -60),
    (_('Urubamba River'), 235, 504, 570, -60),
    (_('Tambo River'), 234, 440, 603, -60),
    (_('Apurimac River'), 233, 526, 692, -45),
    (_('Lake Titicaca'), 232, 650, 763, 0),
    (_('Gulf of Guayaquil'), 231, 127, 171, 0),
    (_('Sechura Bay'), 230, 108, 287, 0),
    (_('Pacific Ocean'), 229, 142, 630, 0)
]

ROUTES = []

STATS = [
    (_('Capital:'), _('Lima') + _("(12º02' S - 77º01' W)")),
    (_('Language:'), _('Spanish') + ' , ' + _('Quechua') + ' , ' + _('Aimará')),
    (_('Government:'), _('Presidential republic')),
    (_('President:'), _('Ollanta Humala Tasso')),
    (_('Prime Minister:'), _('Pedro Cateriano')),
    (_('Independence:'), _('from Spain')),
    ('', _('declared: %s') % _('28 of july of 1821')),
    ('', _('recognized: %s') % _('14 of august of 1879')),
    (_('Area:'), _('1.285.216 km² (20th)')),
    (_('Population:'), _('31.151.643 (40th)')),
    (_('GDP:'), _('USD 217.607 billion (50th)')),
    (_('HDI:'), '%(l)s - %(v)s (%(p)s)' % {'l': _('High'), 'v': _('0,734'), 'p': _('84th')}),
    (_('Currency:'), _('Nuevo sol')),
    (_('Info updated:'), _('5 of april of 2016'))
]

