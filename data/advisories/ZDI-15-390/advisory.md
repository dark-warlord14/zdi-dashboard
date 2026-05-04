# ZDI-15-390: Apple OS X iCloud Account Authentication Elevation Of Privilege Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-390
- **ZDI-CAN:** ZDI-CAN-2996
- **Date:** 2015-08-13
- **CVE:** CVE-2015-3799
- **CVSS:** 7.2
- **CVSS Vector:** AV:L/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-390/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Apple OS X. An attacker must have shell access to exploit this vulnerability, however Guest access is sufficient. The specific flaw exists within the authentication of users who use their iCloud account and password to log in to OS X. Any user is able to change the password of these users without knowing the previous password. This allows an attacker to run arbitrary commands as that user. If the target user is an Admin, the attacker can run arbitrary commands as root.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT201222

## Disclosure Timeline

- 2015-06-10 - Vulnerability reported to vendor
- 2015-08-13 - Coordinated public release of advisory
