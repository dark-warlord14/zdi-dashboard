# ZDI-10-074: Sun Microsystems Directory Server Enterprise ASN.1 Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-074
- **ZDI-CAN:** ZDI-CAN-595
- **Date:** 2010-04-13
- **CVE:** CVE-2010-0897
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Sun Microsystems
- **Affected Products:** Directory Server
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-074/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Sun Microsystems Directory Service Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within Sun Directory Server's LDAP implementation and can be triggered via a malformed LDAP query to the ns_slapd service. When the service decodes the malformed extendedRequest query containing a malformed requestValue string, the application will cause a buffer overflow which can lead to code execution under the context of the service.

## Additional Details

Sun Microsystems has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technology/deploy/security/critical-patch-updates/cpuapr2010.html

## Disclosure Timeline

- 2009-10-27 - Vulnerability reported to vendor
- 2010-04-13 - Coordinated public release of advisory
