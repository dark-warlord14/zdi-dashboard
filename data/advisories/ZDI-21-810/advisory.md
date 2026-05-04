# ZDI-21-810: Adobe Acrobat Pro DC embedDocAsDataObject Type Confusion Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-810
- **ZDI-CAN:** ZDI-CAN-13557
- **Date:** 2021-07-15
- **CVE:** CVE-2021-28643
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Pro DC
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-810/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Adobe Acrobat Pro DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within EScript.api. When parsing the oDoc object, the process does not properly validate user-supplied data, which can result in a type confusion condition. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb21-51.html

## Disclosure Timeline

- 2021-04-30 - Vulnerability reported to vendor
- 2021-07-15 - Coordinated public release of advisory
