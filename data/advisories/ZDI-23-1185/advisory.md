# ZDI-23-1185: (0Day) Maxon Cinema 4D SKP File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1185
- **ZDI-CAN:** ZDI-CAN-21431
- **Date:** 2023-08-24
- **CVE:** CVE-2023-40483
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Maxon
- **Affected Products:** Cinema 4D
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1185/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Maxon Cinema 4D. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of SKP files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

06/15/23 – ZDI requested a vendor PSIRT contact. 07/12/23 – ZDI made another attempt to contact the vendor. 08/17/23 – ZDI attempted to contact the vendor once more using the contact information on their website, as well as trying to reach them on various social platforms. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2023-08-24 - Vulnerability reported to vendor
- 2023-08-24 - Coordinated public release of advisory
