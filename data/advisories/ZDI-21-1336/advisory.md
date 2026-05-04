# ZDI-21-1336: Panda Security Free Antivirus Unnecessary Privileges Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1336
- **ZDI-CAN:** ZDI-CAN-14208
- **Date:** 2021-11-29
- **CVE:** CVE-2021-34998
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Panda Security
- **Affected Products:** Free Antivirus
- **Credit:** Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1336/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Panda Security Free Antivirus. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the use of named pipes. The issue results from allowing an untrusted process to impersonate the client of a pipe. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Panda Security has issued an update to correct this vulnerability. More details can be found at: https://www.pandasecurity.com/en/support/card?id=100077

## Disclosure Timeline

- 2021-06-25 - Vulnerability reported to vendor
- 2021-11-29 - Coordinated public release of advisory
