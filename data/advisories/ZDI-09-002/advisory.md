# ZDI-09-002: Microsoft SMB NT Trans2 Request Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-002
- **ZDI-CAN:** ZDI-CAN-379
- **Date:** 2009-01-13
- **CVE:** CVE-2008-4835
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Microsoft, Microsoft, Microsoft, Microsoft, Microsoft
- **Affected Products:** Windows 2000 SP4, Windows XP, Windows Server 2003, Windows Vista, Windows Server 2008
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-002/
## Vulnerability Details

This vulnerability allows remote attackers to trigger a denial of service condition on vulnerable installations of Microsoft Windows; remote code execution is also theoretically possible. User interaction is not required to exploit this vulnerability. The specific flaw exists in the processing of SMB requests. By specifying malformed values during an NT Trans2 request an attacker can cause the target system to kernel panic thereby requiring a reboot of the system. Further manipulation can theoretically result in remote unauthenticated code execution.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: http://www.microsoft.com/technet/security/bulletin/ms09-001.mspx

## Disclosure Timeline

- 2008-08-14 - Vulnerability reported to vendor
- 2009-01-13 - Coordinated public release of advisory
