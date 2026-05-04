# ZDI-20-1237: IBM Informix spatial Out-Of-Bounds Write Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1237
- **ZDI-CAN:** ZDI-CAN-10580
- **Date:** 2020-10-08
- **CVE:** CVE-2020-4799
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** IBM
- **Affected Products:** Informix
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1237/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of IBM Informix. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the spatial.bld module. When parsing SQL statements, the process does not properly validate user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the informix user.

## Additional Details

IBM has issued an update to correct this vulnerability. More details can be found at: https://www.ibm.com/support/pages/node/6343587

## Disclosure Timeline

- 2020-05-06 - Vulnerability reported to vendor
- 2020-10-08 - Coordinated public release of advisory
