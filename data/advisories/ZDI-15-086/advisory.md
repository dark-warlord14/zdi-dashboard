# ZDI-15-086: Microsoft Windows .LNK DLL Planting Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-086
- **ZDI-CAN:** ZDI-CAN-2681
- **Date:** 2015-03-11
- **CVE:** CVE-2015-0096
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Michael Heerklotz
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-086/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious web page or open a malicious directory or device. The specific flaw exists within the handling of LNK files by the Windows shell. By providing a pair of crafted files, an attacker is able to force the Explorer process to load an arbitrary DLL when displaying file icons in the directory view. This allows an attacker to execute arbitrary code in the context of the Explorer process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS15-020

## Disclosure Timeline

- 2015-01-08 - Vulnerability reported to vendor
- 2015-03-11 - Coordinated public release of advisory
