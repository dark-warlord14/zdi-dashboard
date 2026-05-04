# ZDI-24-582: SEW-EURODRIVE MOVITOOLS MotionStudio XML External Entity Processing Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-582
- **ZDI-CAN:** ZDI-CAN-19094
- **Date:** 2024-06-06
- **CVE:** CVE-2024-1167
- **CVSS:** 5.5
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:N
- **Affected Vendors:** SEW-EURODRIVE
- **Affected Products:** MOVITOOLS MotionStudio
- **Credit:** Esjay (@esj4y)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-582/
## Vulnerability Details

This vulnerability allows remote atttackers to disclose sensitive information on affected installations of SEW-EURODRIVE MOVITOOLS MotionStudio. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of SEWPROJ files. Due to the improper restriction of XML External Entity (XXE) references, a crafted document specifying a URI causes the XML parser to access the URI and embed the contents back into the XML document for further processing. An attacker can leverage this vulnerability to disclose information in the context of the current process.

## Additional Details

SEW-EURODRIVE has issued an update to correct this vulnerability. More details can be found at: https://download.sew-eurodrive.com/download/pdf/31965520.pdf

## Disclosure Timeline

- 2023-08-03 - Vulnerability reported to vendor
- 2024-06-06 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
