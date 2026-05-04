# ZDI-18-551: GE MDS PulseNET Account Java RMI Incorrect Privilege Assignment Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-551
- **ZDI-CAN:** ZDI-CAN-5591
- **Date:** 2018-06-06
- **CVE:** CVE-2018-10611
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/Au:S/C:P/I:P/A:P
- **Affected Vendors:** GE
- **Affected Products:** MDS PulseNET
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-551/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of GE MDS PulseNET. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the configuration of the Remote Method Invocation interface. The interface is not sufficiently protected from low-privileged users. An attacker can leverage this vulnerability to execute code under the context of the service.

## Additional Details

GE has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-151-02

## Disclosure Timeline

- 2018-01-19 - Vulnerability reported to vendor
- 2018-06-06 - Coordinated public release of advisory
- 2018-06-06 - Advisory Updated
