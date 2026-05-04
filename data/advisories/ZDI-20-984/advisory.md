# ZDI-20-984: Adobe Acrobat Reader DC app.measureDialog Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-984
- **ZDI-CAN:** ZDI-CAN-11105
- **Date:** 2020-08-12
- **CVE:** CVE-2020-9697
- **CVSS:** 5.5
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:N
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Reader DC
- **Credit:** Abdul-Aziz Hariri of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-984/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Adobe Acrobat Reader DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the app.measureDialog method. By manipulating a document's actions in JavaScript, an attacker can disclose the base address of EScript.api. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb20-48.html

## Disclosure Timeline

- 2020-05-19 - Vulnerability reported to vendor
- 2020-08-12 - Coordinated public release of advisory
