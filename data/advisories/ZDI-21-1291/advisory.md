# ZDI-21-1291: Open Design Alliance (ODA) ODAViewer DGN File Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1291
- **ZDI-CAN:** ZDI-CAN-14329
- **Date:** 2021-11-10
- **CVE:** CVE-2021-43273
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Open Design Alliance (ODA)
- **Affected Products:** ODAViewer
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1291/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Open Design Alliance (ODA) ODAViewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DGN files. Crafted data in a DGN file can trigger a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Open Design Alliance (ODA) has issued an update to correct this vulnerability. More details can be found at: https://www.opendesign.com/security-advisories

## Disclosure Timeline

- 2021-07-02 - Vulnerability reported to vendor
- 2021-11-10 - Coordinated public release of advisory
