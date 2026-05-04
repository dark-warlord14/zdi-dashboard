# ZDI-22-148: ESET Endpoint Antivirus Unnecessary Privileges Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-148
- **ZDI-CAN:** ZDI-CAN-14162
- **Date:** 2022-01-31
- **CVE:** CVE-2021-37852
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** ESET
- **Affected Products:** Endpoint Antivirus
- **Credit:** Michael DePlante (@izobashi) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-148/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of ESET Endpoint Antivirus. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the use of named pipes. The issue results from allowing an untrusted process to impersonate the client of a pipe. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

ESET has issued an update to correct this vulnerability. More details can be found at: https://support.eset.com/en/ca8223-local-privilege-escalation-vulnerability-fixed-in-eset-products-for-windows

## Disclosure Timeline

- 2021-06-18 - Vulnerability reported to vendor
- 2022-01-31 - Coordinated public release of advisory
