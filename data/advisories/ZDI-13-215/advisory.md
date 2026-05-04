# ZDI-13-215: Microsoft Visio Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-215
- **ZDI-CAN:** ZDI-CAN-1799
- **Date:** 2013-09-11
- **CVE:** CVE-2013-3863
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Office Visio
- **Credit:** G. Geshev
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-215/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Visio. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of VST files. The issue lies in the failure to validate a length specified by the file before using it as a size in a memcpy. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://technet.microsoft.com/security/bulletin/MS13-070

## Disclosure Timeline

- 2013-04-16 - Vulnerability reported to vendor
- 2013-09-11 - Coordinated public release of advisory
