# ZDI-18-913: Novell NetIQ Access Manager dhost Service Shared Memory Section Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-913
- **ZDI-CAN:** ZDI-CAN-6207
- **Date:** 2018-08-10
- **CVE:** CVE-2018-7686
- **CVSS:** 2.1
- **CVSS Vector:** AV:L/AC:L/Au:N/C:N/I:N/A:P
- **Affected Vendors:** Novell
- **Affected Products:** NetIQ Access Manager
- **Credit:** Steven Seeley (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-913/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on vulnerable installations of Novell NetIQ Access Manager. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the processing of information in a shared memory section by the dhost service. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges to the context of SYSTEM.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: https://www.netiq.com/documentation/edirectory-91/edirectory9111_releasenotes/data/edirectory9111_releasenotes.html

## Disclosure Timeline

- 2018-05-16 - Vulnerability reported to vendor
- 2018-08-10 - Coordinated public release of advisory
- 2018-08-10 - Advisory Updated
