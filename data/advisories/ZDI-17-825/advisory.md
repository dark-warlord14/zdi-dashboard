# ZDI-17-825: Hewlett Packard Enterprise Application Performance Management Staging Data Replicator hpbsmsdr Missing Authentication for Critical Function Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-825
- **ZDI-CAN:** ZDI-CAN-4825
- **Date:** 2017-09-26
- **CVE:** CVE-2017-14350
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett Packard Enterprise
- **Affected Products:** Application Performance Management Staging Data Replicator
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-825/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett Packard Enterprise Application Performance Management Staging Data Replicator. The specific flaw exists within the hpbsmsdr web service, which listens on TCP port 29921 by default. The software does not provide any authentication for functionality that can invoke arbitrary classes. An attacker can leverage this vulnerability to execute code under the context of SYSTEM.

## Additional Details

Hewlett Packard Enterprise has issued an update to correct this vulnerability. More details can be found at: http://seclists.org/bugtraq/2017/Sep/31

## Disclosure Timeline

- 2017-05-30 - Vulnerability reported to vendor
- 2017-09-26 - Coordinated public release of advisory
