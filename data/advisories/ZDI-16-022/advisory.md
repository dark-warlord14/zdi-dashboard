# ZDI-16-022: Oracle GoldenGate File Upload Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-022
- **ZDI-CAN:** ZDI-CAN-3040
- **Date:** 2016-01-22
- **CVE:** CVE-2016-0451
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** GoldenGate
- **Credit:** Mike Arnold (Bruk0ut)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-022/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle GoldenGate. Authentication is not required to exploit this vulnerability. The specific flaw exists within the GoldenGate mgr process, which listens on TCP port 7809. By default, the process does not authenticate connecting machines prior to allowing them to write arbitrary files at arbitrary locations on the server. An attacker could leverage this vulnerability to execute arbitrary code under the context of the current user.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/cpujan2016-2367955.html

## Disclosure Timeline

- 2015-07-10 - Vulnerability reported to vendor
- 2016-01-22 - Coordinated public release of advisory
