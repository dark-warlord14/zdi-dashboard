# ZDI-16-156: Microsoft Reader Uninitialized Pointer Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-156
- **ZDI-CAN:** ZDI-CAN-3252
- **Date:** 2016-02-09
- **CVE:** CVE-2016-0046
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Reader
- **Credit:** Jaanus Kp Clarified Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-156/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Reader. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of PDF files. By providing a malformed PDF file, an attacker can cause an uninitialized pointer to be dereferenced. An attacker could leverage this to execute arbitrary code under the context of the process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/ms16-012.aspx

## Disclosure Timeline

- 2015-09-13 - Vulnerability reported to vendor
- 2016-02-09 - Coordinated public release of advisory
