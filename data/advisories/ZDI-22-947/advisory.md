# ZDI-22-947: Parallels Access Agent Time-Of-Check Time-Of-Use Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-947
- **ZDI-CAN:** ZDI-CAN-16134
- **Date:** 2022-07-01
- **CVE:** CVE-2022-34899
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Parallels
- **Affected Products:** Access
- **Credit:** Reno Robert of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-947/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Parallels Access Agent. An attacker must first obtain the ability to execute low-privileged code on the target host system in order to exploit this vulnerability. The specific flaw exists within the Parallels service. By creating a symbolic link, an attacker can abuse the service to execute a file. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

Parallels has issued an update to correct this vulnerability. More details can be found at: https://kb.parallels.com/en/129010

## Disclosure Timeline

- 2021-12-22 - Vulnerability reported to vendor
- 2022-07-01 - Coordinated public release of advisory
