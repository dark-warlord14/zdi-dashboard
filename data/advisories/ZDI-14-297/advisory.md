# ZDI-14-297: Juniper Network and Security Manager XDB Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-297
- **ZDI-CAN:** ZDI-CAN-2151
- **Date:** 2014-08-27
- **CVE:** CVE-2014-3411
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Juniper
- **Affected Products:** Network and Security Manager
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-297/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Juniper Network and Security Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the XDB service. The issue lies in the ability to connect to the service with a remote debugger. An attacker can leverage this vulnerability to execute code under the context of the Java service, which can then be used in conjunction with a privilege escalation vulnerability to gain root privileges.

## Additional Details

Juniper has issued an update to correct this vulnerability. More details can be found at: http://kb.juniper.net/JSA10625

## Disclosure Timeline

- 2014-02-18 - Vulnerability reported to vendor
- 2014-08-27 - Coordinated public release of advisory
