# ZDI-21-580: Microsoft Office Graph Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-580
- **ZDI-CAN:** ZDI-CAN-13497
- **Date:** 2021-05-13
- **CVE:** CVE-2021-31175
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Office
- **Credit:** L4
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-580/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Microsoft Office. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the Graph COM object. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-31175

## Disclosure Timeline

- 2021-04-02 - Vulnerability reported to vendor
- 2021-05-13 - Coordinated public release of advisory
