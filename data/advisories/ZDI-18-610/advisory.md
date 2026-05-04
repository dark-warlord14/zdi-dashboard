# ZDI-18-610: Adobe Acrobat Pro DC ImageConversion EMF EMR_ALPHABLEND Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-610
- **ZDI-CAN:** ZDI-CAN-5968
- **Date:** 2018-07-12
- **CVE:** CVE-2018-4886
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Pro DC
- **Credit:** Ron Waisberg of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-610/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Acrobat Pro DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of EMR_ALPHABLEND records in EMF files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb18-02.html

## Disclosure Timeline

- 2018-05-02 - Vulnerability reported to vendor
- 2018-07-12 - Coordinated public release of advisory
- 2018-07-12 - Advisory Updated
