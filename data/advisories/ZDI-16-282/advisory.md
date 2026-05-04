# ZDI-16-282: (Pwn2Own) Microsoft Edge JavaScript concat Method Uninitialized Memory Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-282
- **ZDI-CAN:** ZDI-CAN-3621
- **Date:** 2016-05-10
- **CVE:** CVE-2016-0191
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Edge
- **Credit:** lokihardt
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-282/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Edge. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the implementation of the JavaScript Array.concat method. By performing certain operations in script, an attacker can cause JavaScript to read uninitialized data from a memory location on the stack. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/ms16-052.aspx

## Disclosure Timeline

- 2016-03-12 - Vulnerability reported to vendor
- 2016-05-10 - Coordinated public release of advisory
