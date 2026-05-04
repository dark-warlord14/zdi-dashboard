# ZDI-21-1286: Open Design Alliance (ODA) ODAViewer DWF File Parsing Use-After-Free Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1286
- **ZDI-CAN:** ZDI-CAN-14352
- **Date:** 2021-11-10
- **CVE:** CVE-2021-43274
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Open Design Alliance (ODA)
- **Affected Products:** ODAViewer
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1286/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Open Design Alliance (ODA) ODAViewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DWF files. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Open Design Alliance (ODA) has issued an update to correct this vulnerability. More details can be found at: https://www.opendesign.com/security-advisories

## Disclosure Timeline

- 2021-07-02 - Vulnerability reported to vendor
- 2021-11-10 - Coordinated public release of advisory
