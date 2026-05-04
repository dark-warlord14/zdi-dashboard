# ZDI-19-209: Adobe Acrobat Pro DC Distiller PostScript File Parsing grestore Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-209
- **ZDI-CAN:** ZDI-CAN-7621
- **Date:** 2019-02-12
- **CVE:** CVE-2019-7069
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Pro DC
- **Credit:** Steven Seeley (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-209/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Acrobat Pro DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of PostScript files. The issue results from the lack of proper validation of user-supplied data, which can result in a type confusion condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb19-07.html

## Disclosure Timeline

- 2018-12-03 - Vulnerability reported to vendor
- 2019-02-12 - Coordinated public release of advisory
