# ZDI-17-907: Adobe Acrobat Pro DC ImageConversion EMF EmfPlusObject Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-907
- **ZDI-CAN:** ZDI-CAN-5218
- **Date:** 2017-11-14
- **CVE:** CVE-2017-16404
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Pro DC
- **Credit:** Ke Liu of Tencent's Xuanwu LAB
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-907/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Acrobat Pro DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of EmfPlusObject objects in EMF files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb17-36.html

## Disclosure Timeline

- 2017-09-26 - Vulnerability reported to vendor
- 2017-11-14 - Coordinated public release of advisory
