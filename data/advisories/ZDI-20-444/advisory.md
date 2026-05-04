# ZDI-20-444: Advantech WebAccess/NMS DatabaseMgmtResource OS Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-444
- **ZDI-CAN:** ZDI-CAN-9826
- **Date:** 2020-04-08
- **CVE:** CVE-2020-10603
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess/NMS
- **Credit:** rgod of 9sg
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-444/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Advantech WebAccess/NMS. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the processing of calls to the ManualDBBackup endpoint. When parsing the filenamebknow parameter, the process does not properly validate a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of SYSTEM.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://www.us-cert.gov/ics/advisories/icsa-20-098-01

## Disclosure Timeline

- 2019-12-17 - Vulnerability reported to vendor
- 2020-04-08 - Coordinated public release of advisory
