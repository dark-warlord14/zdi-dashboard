# ZDI-15-250: (Pwn2Own) Microsoft Internet Explorer DataView Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-250
- **ZDI-CAN:** ZDI-CAN-2831
- **Date:** 2015-06-11
- **CVE:** CVE-2015-1747
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** lokihardt@ASRT
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-250/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within jscript9.dll. When creating a DataView object with an ArrayBuffer, in conjunction with the neuter function, using the ArrayBuffer as an argument, read and write access of arbitrary memory can be achieved. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/ms15-056.aspx

## Disclosure Timeline

- 2015-03-18 - Vulnerability reported to vendor
- 2015-06-11 - Coordinated public release of advisory
