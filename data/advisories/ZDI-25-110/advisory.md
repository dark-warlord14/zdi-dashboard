# ZDI-25-110: SEW-EURODRIVE MOVITOOLS MotionStudio mticomp0 ICP File Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-110
- **ZDI-CAN:** ZDI-CAN-25013
- **Date:** 2025-03-05
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** SEW-EURODRIVE
- **Affected Products:** MOVITOOLS MotionStudio
- **Credit:** Andrea Micalizzi aka rgod (@rgod777)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-110/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of SEW-EURODRIVE MOVITOOLS MotionStudio. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of ICP files by the mticomp0 component. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

SEW-EURODRIVE has issued an update to correct this vulnerability. More details can be found at: https://download.sew-eurodrive.com/download/pdf/31987192.pdf#search=%22security_advisory%22a

## Disclosure Timeline

- 2024-09-19 - Vulnerability reported to vendor
- 2025-03-05 - Coordinated public release of advisory
- 2025-03-05 - Advisory Updated
