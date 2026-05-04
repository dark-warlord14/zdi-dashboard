# ZDI-09-009: EMC AutoStart Backbone Engine Trusted Pointer Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-009
- **ZDI-CAN:** ZDI-CAN-364
- **Date:** 2009-01-23
- **CVE:** CVE-2009-0311
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** EMC
- **Affected Products:** AutoStart
- **Credit:** Manuel Santamarina Suarez
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-009/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on systems with vulnerable installations of EMC AutoStart. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Backbone service (ftbackbone.exe) which listens by default on TCP port 8042. The process trusts a DWORD value from incoming packets which it arbitrarily calls. Exploitation of this issue leads to code execution under the context of the SYSTEM user.

## Additional Details

Customers who are using older versions are advised to upgrade to EMC AutoStart 5.3 SP2 For EMC AutoStart 5.3. SP2 Software navigate to the following location: Powerlink > Support > Software Downloads and Licensing > Downloads A-B > AutoStart

## Disclosure Timeline

- 2008-08-26 - Vulnerability reported to vendor
- 2009-01-23 - Coordinated public release of advisory
