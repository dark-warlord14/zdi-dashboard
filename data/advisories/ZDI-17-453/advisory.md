# ZDI-17-453: Joyent Smart Data Center Docker API Zone Escape Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-453
- **ZDI-CAN:** ZDI-CAN-3853
- **Date:** 2017-07-07
- **CVE:** CVE-2017-10940
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** Joyent
- **Affected Products:** Smart Data Center
- **Credit:** Ben Murphy
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-453/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Joyent Smart Data Center. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the docker API. The process does not properly validate user-supplied data which can allow for the upload of arbitrary files. An attacker can leverage this vulnerability to execute arbitrary code under the context of root.

## Additional Details

Joyent has issued an update to correct this vulnerability. More details can be found at: https://help.joyent.com/hc/en-us/articles/115009649927-Security-Advisory-ZDI-CAN-3853-Docker-File-Overwrite-Vulnerability

## Disclosure Timeline

- 2016-08-25 - Vulnerability reported to vendor
- 2017-07-07 - Coordinated public release of advisory
