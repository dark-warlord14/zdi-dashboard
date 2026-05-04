# ZDI-11-167: Microsoft WINS Service Failed Response Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-167
- **ZDI-CAN:** ZDI-CAN-1075
- **Date:** 2011-05-10
- **CVE:** CVE-2011-1248
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** OS
- **Credit:** Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-167/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows Internet Name Service (WINS). Authentication is not required to exploit this vulnerability. The specific flaw exists within the wins.exe service distributed with Microsoft Windows 2003 Server. This service is designed to resolve NetBIOS requests and accepts connections on port 42. Due to a logic error when handling a socket send exception, certain user-supplied values remain within a stack frame and are re-used in another context. A remote attacker can abuse this flaw to cause a call to LeaveCriticalSection to operate upon a controlled location in memory. Such a condition could lead to remote code execution under the context of the SYSTEM user.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/MS11-035.mspx

## Disclosure Timeline

- 2011-01-21 - Vulnerability reported to vendor
- 2011-05-10 - Coordinated public release of advisory
