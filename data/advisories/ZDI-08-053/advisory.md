# ZDI-08-053: Symantec Veritas Storage Foundation Scheduler Service NULL Session Authentication Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-053
- **ZDI-CAN:** ZDI-CAN-359
- **Date:** 2008-08-14
- **CVE:** CVE-2008-3703
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Symantec
- **Affected Products:** Veritas Storage Foundation
- **Credit:** Tenable Network Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-053/
## Vulnerability Details

This vulnerability allows an attacker to execute arbitrary code on vulnerable installations of Symantec Veritas Storage Foundation. User interaction is not required to exploit this vulnerability. Authentication is not required to exploit this vulnerability. The specific flaw exists in the functionality exposed by the Storage Foundation for Windows Scheduler Service, VxSchedService.exe, which listens by default on TCP port 4888. The management console allows NULL NTLMSSP authentication thereby enabling a remote attacker to add, modify, or delete snapshots schedules and consequently run arbitrary code under the context of the SYSTEM user.

## Additional Details

Symantec has issued an update to correct this vulnerability. More details can be found at: http://www.symantec.com/avcenter/security/Content/2008.08.14a.html

## Disclosure Timeline

- 2008-06-26 - Vulnerability reported to vendor
- 2008-08-14 - Coordinated public release of advisory
