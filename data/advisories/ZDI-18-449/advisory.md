# ZDI-18-449: Adobe Acrobat Pro DC ImageConversion EMF EMR_COMMENT Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-449
- **ZDI-CAN:** ZDI-CAN-5761
- **Date:** 2018-05-15
- **CVE:** CVE-2018-4965
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Acrobat Pro DC
- **Credit:** Steven Seeley (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-449/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Acrobat Pro DC. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of EMR_COMMENT structures embedded inside EMF files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length stack-based buffer. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb18-09.html

## Disclosure Timeline

- 2018-03-06 - Vulnerability reported to vendor
- 2018-05-15 - Coordinated public release of advisory
- 2018-05-15 - Advisory Updated
