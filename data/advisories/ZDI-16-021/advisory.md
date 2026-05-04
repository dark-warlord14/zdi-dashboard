# ZDI-16-021: Oracle GoldenGate Denial of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-021
- **ZDI-CAN:** ZDI-CAN-3039
- **Date:** 2016-01-22
- **CVE:** CVE-2016-0450
- **CVSS:** 5.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:N/I:N/A:P
- **Affected Vendors:** Oracle
- **Affected Products:** GoldenGate
- **Credit:** Mike Arnold (Bruk0ut)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-021/
## Vulnerability Details

This vulnerability allows remote attackers to cause a denial condition on vulnerable installations of Oracle GoldenGate. Authentication is not required to exploit this vulnerability. The specific flaw exists within the GoldenGate mgr process, which listens on TCP port 7809. By default, this process does not require authentication before accepting data delivery and GGSCI commands from a remote machine. This allows for a remote attacker to disable the service or exhaust resources on the target machine.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/cpujan2016-2367955.html

## Disclosure Timeline

- 2015-07-10 - Vulnerability reported to vendor
- 2016-01-22 - Coordinated public release of advisory
