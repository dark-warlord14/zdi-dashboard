# ZDI-16-680: Microsoft Skype DLL Planting Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-680
- **ZDI-CAN:** ZDI-CAN-3577
- **Date:** 2017-04-06
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Skype
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-680/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Skype. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of .skype files. By providing a crafted file, an attacker is able to load an arbitrary DLL. This allows an attacker to execute arbitrary code in the context of the process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/security/cc308575#0419

## Disclosure Timeline

- 2016-03-29 - Vulnerability reported to vendor
- 2017-04-06 - Coordinated public release of advisory
