# ZDI-16-017: Adobe Reader Graphics State Parameter Dictionary Double Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-017
- **ZDI-CAN:** ZDI-CAN-3273
- **Date:** 2016-01-12
- **CVE:** CVE-2016-0935
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Reader
- **Credit:** kdot
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-017/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the ExtGState dictionary within PDFs. The issue lies in the processing of malformed dictionaries leading to a double free. An attacker could leverage this vulnerability to execute arbitrary code under the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/acrobat/apsb16-02.html

## Disclosure Timeline

- 2015-09-03 - Vulnerability reported to vendor
- 2016-01-12 - Coordinated public release of advisory
