# ZDI-18-1263: Oracle Java Usage Tracker usagetracker.properties Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1263
- **ZDI-CAN:** ZDI-CAN-6366
- **Date:** 2018-10-17
- **CVE:** CVE-2018-3211
- **CVSS:** 6.2
- **CVSS Vector:** AV:L/AC:H/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Java
- **Credit:** Nelson William Gamazo Sanchez of Trend Micro Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1263/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Oracle Java. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of a configuration file called usagetracker.properties. By modifying specific properties within this file, it is possible to create an arbitrary file with controlled data when the JVM is started. An attacker can leverage this vulnerability in certain situations to escalate privilege to the level of SYSTEM.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/technetwork/security-advisory/cpuoct2018-4428296.html

## Disclosure Timeline

- 2018-06-08 - Vulnerability reported to vendor
- 2018-10-17 - Coordinated public release of advisory
- 2018-10-17 - Advisory Updated
