# ZDI-11-112: (0 day) Hewlett-Packard Data Protector Media Operations DBServer.exe Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-112
- **ZDI-CAN:** ZDI-CAN-956
- **Date:** 2011-03-23
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Data Protector
- **Credit:** Roi Mallo
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-112/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP Data Protector. Authentication is not required to exploit this vulnerability. The specific flaw exists within the DBServer.exe process which listens by default on TCP port 19813. While parsing a request, the process trusts a user-supplied 32-bit length value and uses it within a memory operation. By specifying large enough values in a packet sent to the service, a remote attacker can execute arbitrary code under the context of the SYSTEM user.

## Additional Details

March 23, 2011 - This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 180 day deadline. -- Mitigations: To mitigate this vulnerability an administrator could restrict communication with this service to known client IP addresses.

## Disclosure Timeline

- 2010-09-24 - Vulnerability reported to vendor
- 2011-03-23 - Coordinated public release of advisory
