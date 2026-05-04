# ZDI-18-931: Crestron Multiple Products CTP Console WIFIWEPPASSWORD Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-931
- **ZDI-CAN:** ZDI-CAN-6172
- **Date:** 2018-08-14
- **CVE:** CVE-2018-11228
- **CVSS:** 9.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Crestron
- **Affected Products:** TSW-760
- **Credit:** Ricky "HeadlessZeke" Lawshae
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-931/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Crestron's Android-based products. Authentication is not required to exploit this vulnerability. The specific flaw exists within the WIFIWEPPASSWORD command of the CTP console. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker could leverage this vulnerability to execute code with root privileges.

## Additional Details

Crestron has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-221-01

## Disclosure Timeline

- 2018-05-08 - Vulnerability reported to vendor
- 2018-08-14 - Coordinated public release of advisory
- 2018-08-14 - Advisory Updated
