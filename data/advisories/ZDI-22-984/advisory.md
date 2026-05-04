# ZDI-22-984: Adobe Acrobat Reader DC Doc printWithParams Use-After-Free Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-984
- **ZDI-CAN:** ZDI-CAN-17167
- **Date:** 2022-07-13
- **CVE:** CVE-2022-34234
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** Suyue Guo and Wei You from Renmin University of China
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-984/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Adobe Acrobat Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of Doc objects. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb22-32.html

## Disclosure Timeline

- 2022-04-27 - Vulnerability reported to vendor
- 2022-07-13 - Coordinated public release of advisory
