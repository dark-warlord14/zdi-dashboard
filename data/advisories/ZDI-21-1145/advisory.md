# ZDI-21-1145: Adobe Acrobat Pro DC getAnnots Type Confusion Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1145
- **ZDI-CAN:** ZDI-CAN-13556
- **Date:** 2021-10-13
- **CVE:** CVE-2021-35986
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Pro DC
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1145/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Adobe Acrobat Pro DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the getAnnots method. When parsing the nPage parameter, the process does not properly validate user-supplied data, which can result in a type confusion condition. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb21-51.html

## Disclosure Timeline

- 2021-05-21 - Vulnerability reported to vendor
- 2021-10-13 - Coordinated public release of advisory
