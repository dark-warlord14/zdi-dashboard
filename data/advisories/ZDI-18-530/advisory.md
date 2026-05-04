# ZDI-18-530: Adobe Acrobat Pro DC HTML2PDF HTML Parsing Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-530
- **ZDI-CAN:** ZDI-CAN-5238
- **Date:** 2018-05-23
- **CVE:** CVE-2018-4998
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Pro DC
- **Credit:** riusksk of Tencent Security Platform Department
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-530/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Acrobat Pro DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of HTML documents inside the HTML2PDF plugin. The issue results from the lack of proper validation of user-supplied data, which can result in a memory corruption condition. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb18-02.html

## Disclosure Timeline

- 2018-01-26 - Vulnerability reported to vendor
- 2018-05-23 - Coordinated public release of advisory
- 2018-05-23 - Advisory Updated
