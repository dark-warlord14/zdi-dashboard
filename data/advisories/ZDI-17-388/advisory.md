# ZDI-17-388: (0Day) Schneider Electric U.motion Builder file_picker Directory Traversal Arbitrary File Upload Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-388
- **ZDI-CAN:** ZDI-CAN-3580
- **Date:** 2017-06-12
- **CVE:** N/A
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/Au:S/C:P/I:P/A:P
- **Affected Vendors:** Schneider Electric
- **Affected Products:** U.motion Builder
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-388/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Schneider Electric U.Motion Builder. User authentication is required to exploit this vulnerability. The specific flaw exists within file_picker.php. The upload path specified by the user is not constrained, so any logged-in user can upload files to any location in the system that is writable by the web service. An attacker can leverage this to execute code on the system in the context of the web server.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 03/29/2016 - ZDI disclosed the vulnerability reports to ICS-CERT (with an expected 'due date' of 07/27/16). 03/29/2016 - ICS-CERT acknowledged that they received them and "sent them on to our contacts at Schneider Electric, and will keep you informed of their progress. We are tracking these issues as ICS-VU-291195." 08/24/2016 - ZDI sent a follow-up inquiry to ICS-CERT requesting the status. 09/08/2016 - ICS-CERT replied requesting more information on one vulnerability report, but said of the others, "they have successfully validated the rest of the vulnerability reports. Unfortunately, they don't expect to have a patch ready until the end of this year." ICS-CERT suggested they would work with the vendor to try to bring this in. 09/19/2016 - ZDI sent a follow-up inquiry to ICS-CERT asking if the vendor was anywhere closer. 10/11/2016 - ZDI sent a follow-up inquiry to ICS-CERT asking if the vendor was anywhere closer and stressed potential 0-day. 12/14/2016 - ZDI sent a follow-up inquiry to ICS-CERT requesting the status. 06/02/2017 - ZDI sent a follow-up inquiry to ICS-CERT requesting the status. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the service should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting. These features are available in the native Windows Firewall, as described in http://technet.microsoft.com/en-us/library/cc725770%28WS.10%29.aspx and numerous other Microsoft Knowledge Base articles.

## Disclosure Timeline

- 2016-04-04 - Vulnerability reported to vendor
- 2017-06-12 - Coordinated public release of advisory
