# ZDI-20-925: (0Day) IBM Informix bts_tracefile Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-925
- **ZDI-CAN:** ZDI-CAN-10332
- **Date:** 2020-07-28
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** IBM
- **Affected Products:** Informix
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-925/
## Vulnerability Details

This vulnerability allows remote attackers to create arbitrary files on affected installations of IBM Informix. Authentication is required to exploit this vulnerability. The specific flaw exists within the bts_tracefile function. When parsing the trace filename, the process does not properly validate a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with ZDI policies. 02/19/20 – ZDI reported the vulnerability to the vendor 02/19/20 – The vendor acknowledged the report 02/27/20 – The vendor requested technical clarification 02/28/20 – ZDI provided additional evidence 03/06/20 – The vendor indicated it was a configuration issue 03/18/20 – ZDI provided additional evidence 07/03/20 – ZDI requested an update 07/21/20 – ZDI requested an update 07/21/20 – The vendor indicated it was a configuration issue 07/21/20 – ZDI provided additional evidence and notified the vendor of the intention to publish the case as a 0-day advisory on 07/28/20 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service. Only the clients and servers that have a legitimate procedural relationship with the service should be permitted to communicate with it.

## Disclosure Timeline

- 2020-02-19 - Vulnerability reported to vendor
- 2020-07-28 - Coordinated public release of advisory
