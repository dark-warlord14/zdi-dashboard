# ZDI-17-723: EMC AppSync Apollo REST Services SQL Injection Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-723
- **ZDI-CAN:** ZDI-CAN-4710
- **Date:** 2017-09-12
- **CVE:** CVE-2017-8015
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:N/A:N
- **Affected Vendors:** EMC
- **Affected Products:** AppSync
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-723/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of EMC Appsync. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be easily bypassed. The specific flaw exists within Apollo REST services, which listens on TCP port 8445 by default. When parsing the query request parameter, the process does not properly validate a user-supplied string before using it to construct SQL queries. An attacker can leverage this vulnerability to disclose sensitive information under the context of SYSTEM.

## Additional Details

EMC has issued an update to correct this vulnerability. More details can be found at: http://seclists.org/fulldisclosure/2017/Sep/14

## Disclosure Timeline

- 2017-05-04 - Vulnerability reported to vendor
- 2017-09-12 - Coordinated public release of advisory
