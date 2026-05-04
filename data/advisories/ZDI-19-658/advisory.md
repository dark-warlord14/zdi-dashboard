# ZDI-19-658: Schneider Electric Zelio Soft 2 ZM2 File Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-658
- **ZDI-CAN:** ZDI-CAN-7895
- **Date:** 2019-07-10
- **CVE:** CVE-2019-6822
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Schneider Electric
- **Affected Products:** Zelio Soft 2
- **Credit:** 9sg Security Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-658/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Schneider Electric ZelioSoft 2. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of ZM2 files. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Schneider Electric has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/icsa-19-190-03

## Disclosure Timeline

- 2019-02-28 - Vulnerability reported to vendor
- 2019-07-10 - Coordinated public release of advisory
