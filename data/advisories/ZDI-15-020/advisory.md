# ZDI-15-020: Microsoft Internet Explorer Ptls6::LsFmtText Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-020
- **ZDI-CAN:** ZDI-CAN-2562
- **Date:** 2015-02-10
- **CVE:** CVE-2015-0037
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** sweetchip@GRAYHASH
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-020/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of arguments passed to the Ptls6::LsFmtText function. By manipulating a document's elements an attacker can access data outside the bounds of an allocated buffer. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS15-009

## Disclosure Timeline

- 2014-10-09 - Vulnerability reported to vendor
- 2015-02-10 - Coordinated public release of advisory
