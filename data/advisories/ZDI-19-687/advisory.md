# ZDI-19-687: (0Day) SolarWinds Orion Network Performance Monitor ExecuteExternalProgram Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-687
- **ZDI-CAN:** ZDI-CAN-8476
- **Date:** 2019-08-05
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** SolarWinds
- **Affected Products:** Orion Network Performance Monitor
- **Credit:** Ron Waisberg of Trend Micro Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-687/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of SolarWinds Orion Network Performance Monitor. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the ExecuteExternalProgram method. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of SYSTEM.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 03/29/19 - ZDI reported the vulnerability to the vendor 03/29/19 – The vendor acknowledged 04/30/19 – The vendor provided an update indicating they were working on a fix 06/03/19 – The vendor provided an update indicating they were working on a fix 07/09/19 – The vendor provided an update indicating they were working on a fix 07/09/19 – ZDI requested an ETA for the fix and reminded the vendor of the due date, 07/27/19 07/10/19 – The vendor indicated the ETA was Q4 and requested an extension 07/10/19 – ZDI suggested the vendor push the release forward to early August and expressed the intention to 0-day publish the report otherwise 07/10/19 – The vendor indicated their next release cycle would be in Q4 07/11/19 – ZDI requested a closer estimate of ‘Q4’ 07/12/19 – The vendor indicated they anticipated October 07/21/19 – ZDI notified the vendor the intention to 0-day the case on 05/08 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2019-03-29 - Vulnerability reported to vendor
- 2019-08-05 - Coordinated public release of advisory
