# ZDI-17-167: Microsoft Edge CTransitionValues Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-167
- **ZDI-CAN:** ZDI-CAN-3934
- **Date:** 2017-03-21
- **CVE:** CVE-2017-0011
- **CVSS:** 2.6
- **CVSS Vector:** AV:N/AC:H/Au:N/C:P/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Edge
- **Credit:** Suto
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-167/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of Microsoft Edge. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the processing of the filter attribute in CSS. By manipulating a document's elements an attacker can trigger a read past the end of an allocated data structure. An attacker could leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/ms17-007.aspx

## Disclosure Timeline

- 2016-09-08 - Vulnerability reported to vendor
- 2017-03-21 - Coordinated public release of advisory
